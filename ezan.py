import playsound, time, requests, http.client, json, datetime, threading   # windoows için.

global now_time, namaz_gun, t_sabah, t_ikindi, t_aksam, t_yatsi, t_ogle

namaz_gun = None
now_time = None

def get_nowtime():
    global now_time, namaz_gun, t_sabah, t_ogle, t_ikindi, t_aksam, t_yatsi

    date = datetime.datetime.now()
    bugun = datetime.datetime.strftime(date,'%x')
    now_time = datetime.datetime.strftime(date,'%H:%M')


    if bugun != namaz_gun:
        namaz_gun = bugun
        t_sabah = 0; t_ogle=0; t_ikindi=0; t_aksam=0; t_yatsi=0


def check_time():
    global now_time, sabah, ogle, aksam, ikindi, yatsi, t_sabah, t_ogle, t_ikindi, t_aksam, t_yatsi
    
    try:
        get_nowtime()

        if now_time == sabah and t_sabah == 0:
            playsound.playsound("C:/Users/ilker.ozmen/Desktop/2.mp3", True)
            t_sabah = 1
            print("sabah: ",now_time )
        if now_time == ogle and t_ogle == 0:
            playsound.playsound("C:/Users/ilker.ozmen/Desktop/2.mp3", True)
            t_ogle = 1
            print("ogle: ",now_time)
        if now_time == aksam and t_aksam == 0:
            t_aksam = 1
            playsound.playsound("C:/Users/ilker.ozmen/Desktop/2.mp3", True)
            print("aksam: ",now_time)
        if now_time == ikindi and t_ikindi == 0:
            t_ikindi = 1
            playsound.playsound("C:/Users/ilker.ozmen/Desktop/2.mp3", True)
            print("ikindi: ",now_time)
        if now_time == yatsi and t_yatsi == 0:
            t_yatsi = 1
            playsound.playsound("C:/Users/ilker.ozmen/Desktop/2.mp3", True)
            print("yatsi: ",now_time)
    finally:
        thread_check_time()

def get_api():
    global now_time, thread_check_time, sabah, ogle, aksam, ikindi, yatsi
    get_nowtime()
    
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
    'content-type': "application/json",
    'authorization': "apikey 4nPQMhyRXmnRKnSy4HtaNz:0lhwk0zvgNakE0soOcXcKi"
    }

    conn.request("GET", "/pray/all?data.city=bursa", headers=headers)

    res = conn.getresponse()
    data = res.read()
    j_son = json.loads(data)

    sabah = j_son["result"][0]['saat']         # sabah namazı
    ogle = j_son["result"][2]['saat']         # öğle namazı
    ikindi = j_son["result"][3]['saat']         # ikindi namazı
    aksam = j_son["result"][4]['saat']         # aksam namazı
    yatsi = j_son["result"][5]['saat']         # yatsi namazı

    # print( now_time +'> '+ sabah +' '+ogle+' '+' '+ikindi+' '+aksam+' '+yatsi)

    # sabah = '17:45'
    # ogle = '17:46'
    # aksam = '17:47'
    # ikindi = '17:48'
    # yatsi = '17:49'
  
      
def thread_check_time():
    t_check_time = threading.Timer(6,check_time)
    t_check_time.daemon = True
    t_check_time.start()


if __name__ == '__main__':
    try:
        get_api()
        thread_check_time()

        while True:
            time.sleep(0.5)

    except Exception as err:
        print(err)

