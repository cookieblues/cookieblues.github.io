setup-arch:
	sudo pacman -S ruby base-devel ruby-erb

local:
	python src/polling_chart.py
	python src/semi_donut_chart.py
	bundle install
	bundle exec jekyll serve
