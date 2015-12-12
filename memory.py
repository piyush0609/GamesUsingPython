# template for "Stopwatch: The Game"

import simplegui


# define global variables
width = 500
height = 500
interval = 100
counter = 0
position = [190, 260]
game_position = [410, 53]
message = "0:00.0"
game_message = "0/0"
clicks = 0
success = 0
running = False

# define helper function that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    t /= 10
    seconds = t % 60
    t /= 60
    minutes = t % 60
    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = "0" + seconds
    return str(minutes) + ':' + seconds + '.' + str(tenths)

# helper function that converts game score to text
def format_game(cl, su):
    return str(su) + '/' + str(cl)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global running
    timer.start()
    running = True

def stop_handler():
    global clicks, success, running
    if running:
        clicks += 1
        if not (counter % 10):
            success += 1
    timer.stop()
    running = False
    
def reset_handler():
    global counter, message, clicks, success, game_message
    timer.stop()
    counter = 0
    message = "0:00.0"
    game_message = "0/0"
    clicks = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    message = format(counter)
    game_message = format_game(clicks, success)
    canvas.draw_text(message, position, 60, "Red")
    canvas.draw_text(game_message, game_position, 60, "Green")
    
# create frame
frame = simplegui.create_frame("Home", width, height)

# register event handlers
start_button = frame.add_button("Start", start_handler, 50)
stop_button = frame.add_button("Stop", stop_handler, 50)
reset_button = frame.add_button("Reset", reset_handler, 50)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()# template for "Stopwatch: The Game"

import simplegui


# define global variables
width = 500
height = 500
interval = 100
counter = 0
position = [190, 260]
game_position = [410, 53]
message = "0:00.0"
game_message = "0/0"
clicks = 0
success = 0
running = False

# define helper function that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    t /= 10
    seconds = t % 60
    t /= 60
    minutes = t % 60
    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = "0" + seconds
    return str(minutes) + ':' + seconds + '.' + str(tenths)

# helper function that converts game score to text
def format_game(cl, su):
    return str(su) + '/' + str(cl)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global running
    timer.start()
    running = True

def stop_handler():
    global clicks, success, running
    if running:
        clicks += 1
        if not (counter % 10):
            success += 1
    timer.stop()
    running = False
    
def reset_handler():
    global counter, message, clicks, success, game_message
    timer.stop()
    counter = 0
    message = "0:00.0"
    game_message = "0/0"
    clicks = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    message = format(counter)
    game_message = format_game(clicks, success)
    canvas.draw_text(message, position, 60, "Red")
    canvas.draw_text(game_message, game_position, 60, "Green")
    
# create frame
frame = simplegui.create_frame("Home", width, height)

# register event handlers
start_button = frame.add_button("Start", start_handler, 50)
stop_button = frame.add_button("Stop", stop_handler, 50)
reset_button = frame.add_button("Reset", reset_handler, 50)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()# template for "Stopwatch: The Game"

import simplegui


# define global variables
width = 500
height = 500
interval = 100
counter = 0
position = [190, 260]
game_position = [410, 53]
message = "0:00.0"
game_message = "0/0"
clicks = 0
success = 0
running = False

# define helper function that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    t /= 10
    seconds = t % 60
    t /= 60
    minutes = t % 60
    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = "0" + seconds
    return str(minutes) + ':' + seconds + '.' + str(tenths)

# helper function that converts game score to text
def format_game(cl, su):
    return str(su) + '/' + str(cl)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global running
    timer.start()
    running = True

def stop_handler():
    global clicks, success, running
    if running:
        clicks += 1
        if not (counter % 10):
            success += 1
    timer.stop()
    running = False
    
def reset_handler():
    global counter, message, clicks, success, game_message
    timer.stop()
    counter = 0
    message = "0:00.0"
    game_message = "0/0"
    clicks = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    message = format(counter)
    game_message = format_game(clicks, success)
    canvas.draw_text(message, position, 60, "Red")
    canvas.draw_text(game_message, game_position, 60, "Green")
    
# create frame
frame = simplegui.create_frame("Home", width, height)

# register event handlers
start_button = frame.add_button("Start", start_handler, 50)
stop_button = frame.add_button("Stop", stop_handler, 50)
reset_button = frame.add_button("Reset", reset_handler, 50)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()