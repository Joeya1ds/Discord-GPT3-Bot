import os 

def create_log_file(log_path: str, user_id: int) -> None:

    '''
        Creates a log file for a user if it does not already exist.
    
        Args:
            * log_path (str): The path to the directory where the log files are stored.
            * user (int): The ID of the user.
    '''

    if not os.path.exists(f'{log_path}/{user_id}'):
        print(f'User with ID: {user_id} does not have a log file created. Creating.')
        os.makedirs(f'{log_path}/{user_id}')


def append_log(log_path: str, user_id: int, prompt: str) -> None:

    '''
        Appends a log entry to the log file.
    
        Args:
            * log_path (str): The path to the directory where the log files are stored.
            * user (int): The ID of the user.
            * prompt (str): The user's prompt to be written to the log file.
    '''

    with open(f'{log_path}/{user_id}/{user_id}.txt', 'a') as f:
        f.write(f'{user_id} wrote: "{prompt}"')


def append_token_log(log_path: str, user_id: int, n_token: int) -> None:

    '''
        Appends number of tokens being used to the log file.
    
        Args:
            * log_path (str): The path to the directory where the log files are stored.
            * user_id (int): The ID of the user.
            * token (int): The number of the token being used.
    '''

    with open(f'{log_path}/{user_id}/{user_id}.txt', 'a') as f:
        f.write(f' using {n_token} tokens.')


def append_warning_log(log_path: str, user_id: int) -> None:

    '''
        Appends a warning message to the log file indicating that the user's content was flagged by the OpenAI Moderation API.
    
        Args:
            * log_path (str): The path to the directory where the log files are stored.
            * user_id (int): The ID of the user.
    '''

    with open(f'{log_path}/{user_id}/{user_id}.txt', 'a') as f:
        f.write(f' and was flagged by the OpenAI Moderation API!')


def append_newline_log(log_path: str, user_id: int) -> None:

    '''
        Appends a newline character to the log file.
    
        Args:
            * log_path (str): The path to the directory where the log files are stored.
            * user_id (int): The ID of the user.
    '''

    with open(f'{log_path}/{user_id}/{user_id}.txt', 'a') as f:
        f.write(f'\n')