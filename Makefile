SHELL:= $(shell which bash)

ELFINDERDIR=elFinder
ELFINDERLOC=git://github.com/josephtate/elFinder.git
TRUNKVER=trunk
BASEDIR=tw2/jqplugins/elfinder
STATICDIR=$(BASEDIR)/static/jquery/plugins/elfinder/$(TRUNKVER)

update: $(ELFINDERDIR)
	cd $(ELFINDERDIR) && git pull -u $(ELFINDERLOC)
	cd $(ELFINDERDIR)/src && $(MAKE) elfinder
	cp $(ELFINDERDIR)/src/connectors/python/elFinder.py $(BASEDIR)/connector
	cp $(ELFINDERDIR)/src/connectors/python/connector.py $(BASEDIR)/connector/cgi.py
	mkdir -p $(STATICDIR)/js
	mkdir -p $(STATICDIR)/css
	mkdir -p $(STATICDIR)/images
	cp $(ELFINDERDIR)/src/elfinder.css $(STATICDIR)/css
	cp $(ELFINDERDIR)/src/elfinder.full.js $(STATICDIR)/js
	cp $(ELFINDERDIR)/src/elfinder.min.js $(STATICDIR)/js
	rsync -r --delete $(ELFINDERDIR)/src/images/ $(STATICDIR)/images/

$(ELFINDERDIR):
	@[ -d $(ELFINDERDIR) ] || { git clone $(ELFINDERLOC) $(ELFINDERDIR); }

clone: $(ELFINDERDIR)
