from flask import flash, redirect, render_template, Response

from . import app, db
from .constants import BASE_URL
from .forms import MyForm
from .models import URLMap
from .utils import create, get_unique_id


@app.route('/', methods=('GET', 'POST'))
def index_view() -> Response:
    form = MyForm()
    if form.validate_on_submit():
        if not form.custom_id.data:
            form.custom_id.data = get_unique_id(URLMap, URLMap.short)
        create(db, URLMap(
            original=form.original_link.data,
            short=form.custom_id.data,
        ))
        flash('Ваша новая ссылка готова:')
        flash(f'{BASE_URL + form.custom_id.data}', 'url')
    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def redirection(short_id) -> Response:
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original
    )