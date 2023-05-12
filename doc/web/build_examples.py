#!/usr/bin/env python3
import pystache as TPL
import itertools
import markdown
import glob
import re

from build_layout import *
from pathlib import Path

def build_example(file_path, url):
  print(f"> Building page: /examples/{url}")

  tpl = Path("example.tpl.html").read_text()
  path = f"/examples/{url}"
  env = {
      "example_url": url,
      "example_src": Path(file_path).read_text(),
      "example_file": f"{url}.clp",
      "title": f"Example: {url}",
  }

  html = TPL.render(tpl, env)
  write_page(path, html, title=env["title"])
  copy_file(f"{path}.svg", re.sub("\.clp$", ".svg", file_path))

def build_example_list(examples):
  tpl = """
    <h1>Examples</h1>
    <p>
      This page contains a list of example charts generated by clip to show you
      what's possible. Each example links to the clip source that generated it.
    </p>

    {{#list}}
    <h2>{{section}}</h2>
    <section class="examples">
      {{#files}}
        <figure class="example">
          <a href="/examples/{{file}}"><img src="/examples/{{file}}.svg"></a>
          <figcaption>
            <h3>{{title}}</h3>
            {{{desc}}}
            <p>
              <em>Source:</em> <a href="/examples/{{file}}">{{file}}</a>
            </p>
          </figcaption>
        </figure>
      {{/files}}
    </section>
    {{/list}}
  """
  env = {
    "list": examples,
  }

  write_page("/examples", TPL.render(tpl, env), title="Example Gallery", article_class="wide")

def main():
  examples_path = "../../clip-examples"
  examples_list_path = os.path.join(examples_path, "examples.yaml")

  if not os.path.exists(examples_list_path):
    print("> The clip-examples repo was not found; not building examples...")
    return

  examples = yaml.load(Path(examples_path, "examples.yaml").read_text())
  for s in examples:
    for e in s["files"]:
      e.setdefault("title", e["file"])
      e["desc"] = markdown.markdown(e.get("desc", ""))

  for f in glob.glob(f"{examples_path}/**/*.clp"):
    build_example(f, re.sub("\.clp$", "", f[(len(examples_path) + 1):]))

  build_example_list(examples)

main()
