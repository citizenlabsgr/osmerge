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
