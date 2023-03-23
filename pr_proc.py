from pr_io import pr_io
class pr_proc:
    def __init__(self):
        pass

    @classmethod
    def union(self,email_list):
        email_counts = {}
        for mail in email_list:
            if mail not in email_counts:
                email_counts[mail] = 1
        return email_counts.keys(), len(email_counts)

    @classmethod
    def intersect(self,email_list):
        email_counts = {}
        for mail in email_list:
            if mail not in email_counts:
                email_counts[mail] = 1
            else:
                email_counts[mail] += 1
        keys_list = [keys for keys, values in email_counts.items() if values > 1 ]
        return keys_list, len(keys_list)

    @classmethod
    def minus(self,email_list):
        email_counts = {}
        for mail in email_list:
            if mail not in email_counts:
                email_counts[mail] = 1
            else:
                email_counts[mail] += 1

        keys_list = [keys for keys, values in email_counts.items() if values == 1]
        return keys_list, len(keys_list)
