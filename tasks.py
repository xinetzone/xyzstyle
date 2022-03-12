from invoke import Collection, task
from _docs import docs, write


@task
def install(ctx, name='doc'):
    # --use-feature=in-tree-build
    ctx.run(f'pip install .[{name}] ')


ns = Collection(docs, write, install)
