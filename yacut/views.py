from flask import flash, redirect, render_template, Response

from . import app, db
from .constants import BASE_URL
from .forms import MyForm
from .models import URLMap
from .utils import get_unique_id


@app.route('/', methods=('GET', 'POST'))
def index_view() -> Response:
    form = MyForm()
    if form.validate_on_submit():
        if not form.custom_id.data:
            form.custom_id.data = get_unique_id(URLMap, URLMap.short)
        URLMap().create(db, form.data, validation=False)
        flash('Ваша новая ссылка готова:')
        flash(f'{BASE_URL + form.custom_id.data}', 'url')
    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def redirection(short_id) -> Response:
    return redirect(URLMap().get_original_link(short_id, api=False))