import logging
import sys
# from contextlib import contextmanager

# import xlrd
# import xlwt


def use_logger(name: str, level: str = 'INFO'):
    logger = logging.getLogger(name)
    fh = logging.FileHandler(f'{name}.log', encoding='utf-8')
    sh = logging.StreamHandler(stream=sys.stdout)
    formater = logging.Formatter(
        "%(asctime)s  %(name)s %(levelname)s  %(message)s")
    fh.setFormatter(formater)
    sh.setFormatter(formater)
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.setLevel(eval(f"logging.{level}"))
    return logger


# def excel(filename: str, sheet: str, option: str='r'):
#     if option == 'r':
#         workbook=xlrd.open_workbook(filename)
#         if isinstance(sheet, str):
#             sheet=workbook.sheet_by_name(sheet)
#         elif isinstance(sheet, int):
#             sheet=workbook.sheet_by_index(sheet)


#     elif option == 'w':
#         workbook=xlwt.Workbook(filename, encoding="utf-8")
#         sheet =
#         pass
#     else:
#         pass
