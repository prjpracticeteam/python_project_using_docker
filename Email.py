spl_chr_case1 = '!@#$%^&*()_+={}[]|\:;"<>,.?/~`'


def is_prefix_valid(prefix: str):
    return any(i in spl_chr_case1 for i in prefix)


def is_case_valid(prefix: str):
    return any(i.isupper() for i in prefix)


def is_valid_domain(domain: str):
    return (2 <= len(domain) <= 7) and is_prefix_valid(domain)