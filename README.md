The library for easy checker writing for [ForcAD](https://github.com/pomo-mondreganto/ForcAD) Attack-Defence checksystem.

It's compatible with Hackerdom checksystem, too. 

Import it with `from checklib import *` and have access to:

- `TaskStatus` enum with exit codes for action results
- `cquit(status, public='', private=public)` function to 
throw the specified status code and exit, passing public and 
private checker information to checker 
- `assert_*()` functions to ease up the validation of returned data
- `rnd_*()` functions to generate random data like usernames and user agents
- `handle_exception` context manager to handle block exceptions and `cquit` on failure
- `check_response`, `get_text` and `get_json` functions to validate `requests` responses
- `get_initialized_session` function to get `requests` session with random user agent
- `Checker` class for `gevent_optimized` checkers in `ForcAD`

Pull requests are gladly accepted.

Supported python versions: `3.6.8+`.  