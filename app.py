import streamlit as st
import wandb

api = wandb.Api()
artifacts_type = api.artifact_type("model", f'nuvilabs/nuvi_lightning_boxinst')


def list_project_models(artifacts_type):
    models = []
    for collection in artifacts_type.collections():
        for artifact in collection.versions():
            models.append(artifact.name)
    return models


PROJECT = "nuvi_lightning_boxinst"


html = """
<!DOCTYPE html>
<html>
<style>
    html, body { height: 100%; }
    body { overflow: hidden; margin: 0; }
    iframe { height: 100%; width: 100%; frameborder: 0; }
</style>
<body>
<iframe src="https://share.streamlit.io/tcapelle/spacy_streamlit/app.py">
  <p>Your browser does not support iframes.</p>
</iframe>
</body>
</html>
"""


with wandb.init(project=PROJECT):
    wandb.log({"spacy_app":wandb.Html(html)})
