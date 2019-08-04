import os

def Paths(current_dir, toe_file):
    current_dir    = current_dir
    toe_file       = toe_file
    start_file_loc = os.path.join(str(current_dir), toe_file)
    return start_file_loc

def Start_up_msg(current_dir, toe_file, start_file_loc):
    msg = '''- - - - - SETTINGS - - - - - -
current dir         | {dir}
current file        | {toe}
current start_file  | {start}
- - - - - - - - - -  - - - - -
'''.format(dir=current_dir, toe=toe_file, start=start_file_loc)
    return msg

def Launch(**kwargs):
    envVar          = kwargs.get('envVar')
    envVal          = kwargs.get('envVal')
    target_file     = kwargs.get('targetFile')

    os.environ[envVar]  = envVal
    os.startfile(target_file)

    msg                 = '''
STARTING - - - - - - - - - - - -
File            : {file}
Env-Variable    : {var}
Env-Value       : {val}
- - - - - - - - - - - - - - - -'''.format(  file=target_file, 
                                            var=envVar, 
                                            val=envVal)
    return msg

def Start_up(**kwargs):
    current_dir     = kwargs.get('current_dir')
    toe_file        = kwargs.get('toe_file')
    launch_args     = kwargs.get('launch_args')

    start_file_loc  = Paths(current_dir, toe_file)
    print(Start_up_msg(current_dir, toe_file, start_file_loc))
    
    for each_set in launch_args:
        envVar = each_set.get('envVar')
        envVal = each_set.get('envVal')

        launch_event = Launch(envVar=envVar, envVal=envVal, targetFile=start_file_loc)
        print(launch_event)
