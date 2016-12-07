from pathlib import Path


GITIGNORE = """

/tmp

"""

MAKEFILE = """

.PHONY: all
all: build

# PIPELINE #####################################################################

.PHONY: build
build: docs/osmerge.geojson

docs/osmerge.geojson: tmp/merged.json
    osmerge convert $< $@

tmp/merged.json: tmp/filtered.json osmerge.csv
    osmerge merge $< $@

tmp/filtered.json: tmp/base.json osmerge.yml
    osmerge filter $< $@

tmp/base.json: osmerge.yml
    osmerge download $@

# CLEANUP ######################################################################

.PHONY: clean
clean:
    rm -rf tmp

"""

INDEX = """

<!-- TBD -->

"""

GEOJSON = """

{}

"""


class Project(object):

    @classmethod
    def generate(cls):
        root = Path.cwd()

        with root.joinpath(".gitignore").open('w') as stream:
            stream.write(GITIGNORE.strip() + '\n')
        with root.joinpath("Makefile").open('w') as stream:
            stream.write(MAKEFILE.strip() + '\n')

        docs = Path("docs")
        docs.mkdir(parents=True, exist_ok=True)

        with docs.joinpath("index.html").open('w') as stream:
            stream.write(INDEX.strip() + '\n')
        with docs.joinpath("osmerge.geojson").open('w') as stream:
            stream.write(GEOJSON.strip() + '\n')
