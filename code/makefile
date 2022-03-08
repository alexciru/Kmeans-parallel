run:
	python3 main.py

clean:
	@echo "clenaning .pyc and output files"
	rm *.pyc
	rm output/*

plot:
	gnuplot set datafile sep ','
	gnuplot plot "./file.dat" u 1:2:3 with points pt 7 ps 0.5 palette
