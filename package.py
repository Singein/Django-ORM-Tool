from pycman.utils.common import datetime_format

package = {
    'name': 'dotlib',
    'version': '0.0.8',
    'author': 'singein',
    'email': 'singein@outlook.com',
    'scripts': {
        'default': "echo default",
        'tests': f'pytest tests -n=auto --html=test_reports/test-report-{datetime_format()}.html --self-contained-html'
    }
}
