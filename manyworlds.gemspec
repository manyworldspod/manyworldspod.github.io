# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "manyworlds"
  spec.version       = "1.0.0"
  spec.authors       = ["Alex Urban"]
  spec.email         = ["many.worlds.pod@protonmail.com"]

  spec.summary       = "A minimalist Jekyll theme for the Where Many Worlds Fit podcast"
  spec.homepage      = "https://github.com/manyworldspod/manyworldspod.github.io"
  spec.license       = "CC0-1.0"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README|CHANGELOG)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.2"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.16"
  spec.add_runtime_dependency "jekyll-paginate-v2", "~> 3.0"
  spec.add_runtime_dependency "jekyll-sitemap", "~> 1.4"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.8"

end
