import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial position, velocity, and speed
x, y = 0, 0
vx, vy = 0, 0
speed = 1
paused = False

# Axis boundaries
xmin, xmax = -50, 50
ymin, ymax = -50, 50

# Store position history
positions = [(x, y)]

# Function to update position
def update(frame):
    global x, y, vx, vy, paused, speed
    if not paused:  # move only if not paused
        new_x = x + vx * speed
        new_y = y + vy * speed

        # Check boundaries: stop at the wall
        if xmin <= new_x <= xmax:
            x = new_x
        else:
            vx = 0  # stop movement when hitting x wall

        if ymin <= new_y <= ymax:
            y = new_y
        else:
            vy = 0  # stop movement when hitting y wall

        positions.append((x, y))

    line.set_data([p[0] for p in positions], [p[1] for p in positions])
    return line,

# Handle keyboard controls
def on_key(event):
    global vx, vy, paused, speed
    if event.key == "up":
        vx, vy = 0, 1
    elif event.key == "down":
        vx, vy = 0, -1
    elif event.key == "left":
        vx, vy = -1, 0
    elif event.key == "right":
        vx, vy = 1, 0
    elif event.key == "enter":   # stop immediately
        vx, vy = 0, 0
    elif event.key == "space":   # toggle pause/resume
        paused = not paused
    elif event.key == "escape":  # close window
        plt.close()
    elif event.key == "+":       # increase speed
        speed += 1
        print(f"Speed increased to {speed}")
    elif event.key == "-":       # decrease speed
        if speed > 1:
            speed -= 1
            print(f"Speed decreased to {speed}")

# Plot setup
fig, ax = plt.subplots()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
line, = ax.plot([], [], "bo-", markersize=6)

fig.canvas.mpl_connect("key_press_event", on_key)

ani = animation.FuncAnimation(fig, update, interval=200, blit=True)
plt.show()
