
def login_required(fn):
    @functools.warps(fn)
    def inner(*args, **kwargs):
        if session.get('logged_in'):
           return fn(*args, **kwargs)
        return redirect(url_fr('login',next=required.path))
    return inner

@app.route('/login/', methds=['GET', 'POST'])
def login():
    next_url = request.args.get('next') or request.form.get('next')
    if request.method =='POST' and request.form.get('password'):
        password = request.form.get('password')
        if password == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            session.parmanent = True #use cokies to store session.
            flash('you are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            flash('Incorrect password.', 'danger')
    return render_template('login.html',next_url=next_url)



@app.route('/logout/', methods=['GET','POST']) 
def logout():
    if request.method == 'POST':
        session.clear()
        return redirect(url_for('login'))
    return render_template('logout.html') 


@app.route('/')
def index():
    search_query = request.args.get('q')
    if search_query:
        query = Entry.search(search_query)
    else:
        query = Entry.public().order_by(Entry.timestamp.desc())
    return object_list('index.html', query, search=search_query) 
