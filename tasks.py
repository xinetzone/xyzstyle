from invoke import Collection, task
from _docs import docs, write


@task
def init(ctx):
    ctx.run('pip install .[doc] --use-feature=in-tree-build')


ns = Collection(docs, write, init)
