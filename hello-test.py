import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label('Hello, Class', font_size=36, x=200, y=100)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
   