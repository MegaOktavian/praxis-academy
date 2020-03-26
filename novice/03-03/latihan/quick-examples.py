from jinja2 import Template

t = Template("Hello {{ something }}!")
t.render(something="World")

t = Template("My favorite numbers: {% for n in range(1,100) %}{{n}} " "{% endfor %}")
t.render()