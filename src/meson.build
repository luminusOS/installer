python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'misticetos.in',
  output: 'misticetos',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

misticetos_sources = [
  '__init__.py',
  'main.py',
  'welcome.py',
  'header.py',
  'location.py',
]

install_data(misticetos_sources, install_dir: moduledir)
