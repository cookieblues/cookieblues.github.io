setup-arch:
	sudo pacman -S ruby base-devel ruby-erb

local:
	bundle install
	bundle exec jekyll serve
