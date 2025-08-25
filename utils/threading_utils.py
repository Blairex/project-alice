import threading

def run_in_thread(target, *args):
    thread = threading.Thread(target=target, args=args)
    thread.start()
    return thread
# tweak: 1755283524
# tweak: 1755283527
# tweak: 1755283527
# tweak: 1755283537
    # TODO: improve this logic
    # debug log 1757051891
    print('trace 1757051892')
