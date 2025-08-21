import copy

# ---------- Default arguments ----------
def sum_func(c, a=10, b=20):  # default arguments must be at the end
    return a + b + c

x = sum_func(30)
print(x)


# ---------- Positional vs Keyword arguments ----------
def func(a, b, c):
    print(a, b, c)

func(10, 20, 30)                 # positional arguments
func(c=30, a=20, b=10)           # keyword arguments


# ---------- Mixture of keyword & positional ----------
# Parameters before "/" are positional-only
# Parameters after "*" are keyword-only
def fun(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

fun(10, 20, c=30, d=40, f=20, e=45)


# ---------- Arbitrary positional arguments (*args) ----------
def func_args(name, *args):  # args is always a tuple
    print(name, args, type(args))

func_args("Yash", 1, 2, 3, 4, 5, 6, 7, 8)
func_args("Yash", [1, 2, 3, 4, 5])


# ---------- Arbitrary keyword arguments (**kwargs) ----------
def func_kwargs(name, **kwargs):  # kwargs is always a dict
    print(name, kwargs, type(kwargs))

func_kwargs("Yash", a=10, b=20, c=30)


# ---------- Pass by object reference (immutables) ----------
def fun_val_ref(a, b, c):
    a = a + 1
    b += 1
    c += 1
    print(a, b, c, "Inside")

a = 10
b = 20
c = 30
fun_val_ref(a, b, c)   # behaves like pass-by-value for immutables
print(a, b, c, "Outside")


# ---------- Pass by object reference (immutables: strings) ----------
def fun2(a, b, c):
    a += "1"
    b += "2"
    c += "3"
    print(a, b, c, "Inside")

a = "yash"
b = "mundra"
c = "rinku"
fun2(a, b, c)
print(a, b, c, "Outside")


# ---------- Pass by object reference (mutables) ----------
def func3(l):
    l.append(10)
    print(l, "Inside")

p = [1, 2, 3]
func3(p)                 # modifies original list
func3(p.copy())          # shallow copy
func3(copy.deepcopy(p))  # deep copy
print(p, "Outside")


# ---------- Scope: global vs local ----------
x = 100
y = 200
def fun_scope():
    print(x)
fun_scope()
print(x)


def fun_scope2():
    x = 200   # local variable shadows global
    x += 100
    print(x, y)

fun_scope2()
print(x, y)


# ---------- LEGB rule (Local → Enclosing → Global → Built-in) ----------
y = 200
def fun_legb():
    x = 100
    z = 100
    def gun():
        print(x, y, z)  # finds x, z in enclosing scope; y in global
    gun()
fun_legb()


# ---------- nonlocal & global ----------
y = 100
def f():
    x = 100
    def g():
        nonlocal x     # modifies x from enclosing scope (f)
        x = 200
        print(x, "in g")
        global y       # modifies global y
        y = 300
        print(y, "in g")
        z = y
        print(z)
    g()
    print(x, "in f")

f()
print(y, "changed as this global y only used inside the function g")


