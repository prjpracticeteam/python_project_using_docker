import time
import sys
from pr_proc import pr_proc
from pr_io import pr_io
import parser


class minus(pr_proc):

    def __init__(self, file_in):
        super().__init__()
        self.list_1 = pr_io.readfile(file_in[1])
        self.list_2 = pr_io.readfile(file_in[2])
        self.result = file_in[3]

    def minus(self):
        write_file = pr_io
        if self.list_1[1] and self.list_2[1] > 0:
            result_data = pr_proc.minus(self.list_1[0] + self.list_2[0])
            write_file.writefile(self.result, result_data[0])
            return [self.list_1[1],self.list_2[1],result_data[1]]
        else:
            raise Exception("Make sure, the given input files has the data ...")


if __name__ == '__main__':
    try:
        start_time = time.time()
        if len(sys.argv) == 4:
            minus_pr = minus
            res_len = minus_pr(sys.argv).minus()
            print(f"Output: Process Name: Minus, {sys.argv[1]}: {res_len[0]}, {sys.argv[2]}: {res_len[1]}, "
                  f"{sys.argv[3]}: {res_len[2]}, Time taken: {int(time.time() - start_time)}")
            sys.exit(0)
        else:
            raise Exception("The parameters are not matching", parser.parser())
    except FileNotFoundError as file_err:
        print(file_err)
    except ValueError as val_err:
        print(val_err)
    except Exception as ex:
        print(ex)
    finally:
        print(f"Process completed !.. Time taken: {int(time.time() - start_time)}")
