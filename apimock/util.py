# coding=utf-8



def message(msg, *args, **kwargs):
    _print('MESSAGE', msg, *args, **kwargs)


def _print(tag, msg, *args, **kwargs):
    print('%-8s %s' % (tag, msg), *args, **kwargs)
