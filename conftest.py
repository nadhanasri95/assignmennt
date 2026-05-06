def pytest_configure(config):
    config.option.log_cli = True
    config.option.log_file = 'google_test.log'
    config.option.log_file_level= 'INFO'