slides = ane-doppler

all: build/${slides}.pdf

plots: plots/runtime.pdf plots/spectrum.pdf plots/quadrature.pdf \
	plots/error_U238_n,tot.pdf plots/error_U235_n,totf.pdf \
	plots/error_FE56_n,tot.pdf plots/griderror.pdf \
	plots/otf.pdf

plots/error_%.pdf: plots/error.py
	cd plots; python error.py

plots/otf.pdf: plots/otf.py
	cd plots; python otf.py

plots/griderror.pdf: plots/griderror.py
	cd plots; python griderror.py

plots/quadrature.pdf: plots/quadrature.py
	cd plots; python quadrature.py

plots/runtime.pdf: plots/runtime.py
	cd plots; python runtime.py

plots/spectrum.pdf: plots/spectrum.py
	cd plots; python spectrum.py ../testing/beavrs/statepoint.500.h5

build/${slides}.pdf: ${slides}.tex references.bib plots
	mkdir -p build
	pdflatex --output-directory=build -halt-on-error $<
	bibtex build/${slides}
	pdflatex --output-directory=build -halt-on-error $<
	pdflatex --output-directory=build -halt-on-error $<

clean:
	rm -rf build

.PHONY: all plots clean
