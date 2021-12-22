import time 

starttime = time.time()
'''
関数の実行時間を実行後に表示する run_time( )デコレータを作成する。 
呼び出した関数の実行時間を表示する
テスト用の関数を作成し、実行時間を表するmain部を作成する。
'''
def run_time(func): 
    def funcname(*args,**kwargs):
        starttime = time.time()
        result = func(*args,**kwargs)
        '''実行関数と実行時間を表示'''
        print(f'実行関数:{func.__name__}実行時間:{time.time() - starttime}')
        return result
    return funcname
#実行時間[time.time() - starttrim]
# main 
@run_time 
def test(n): 
    for i in range(n): 
        time.sleep(i) 


test(3) 
test(5)