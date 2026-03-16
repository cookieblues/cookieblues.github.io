setup-arch:
	sudo pacman -S ruby base-devel ruby-erb
	gem install bundler
	export GEM_HOME="$(gem env user_gemhome)"
	export PATH="$PATH:$GEM_HOME/bin"

local:
	uv run python src/polling_chart.py
	uv run python src/semi_donut_chart.py
	uv run python src/current_mandate_histogram.py
	uv run python src/uncertainty.py
	bundle install
	bundle exec jekyll serve
