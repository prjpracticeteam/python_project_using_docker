import os
import Email as email


class pr_io:
    def __init__(self):
        pass

    @classmethod
    def readfile(cls, file_name):
        if os.path.exists(file_name):
            file_read = open(file_name, 'r').readlines()
            return file_read, len(file_read) if len(file_read) > 0 else False
        else:
            raise FileNotFoundError(
                f"Make sure the File input file is exist in the given location, \n 1. File not found \n 2. Check "
                f"whether the file name or path correct")

    @classmethod
    def writefile(cls, file_name, data):
            return open(file_name, 'w').writelines(data)

    @classmethod
    def valid_mail(cls, mail):
        if '@' not in mail:
            raise ValueError("Invalid email address: missing @ symbol")
        prefix, suffix = mail.split('@')
        if email.is_prefix_valid(prefix) and email.is_case_valid(prefix) and email.is_valid_domain(suffix[1]):
            return True
        else:
            return False

if __name__ == '__main__':
    pr_io