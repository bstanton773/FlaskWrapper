from app import app
from flask import render_template
from app.forms import TVSearchForm
from app.wrappers import TVMazeAPI

client = TVMazeAPI()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TVSearchForm()
    show_list = None
    if form.validate_on_submit():
        show = form.title.data
        show_list = client.search_shows(show)
    return render_template('index.html', form=form, show_list=show_list)


@app.route('/episodes/<show_id>')
def episodes(show_id):
    show = client.get_show_info(show_id)
    episodes = client.get_show_episodes(show_id)
    return render_template('episodes.html', show=show, episodes=episodes)
