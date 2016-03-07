# Ansible Role: graphite-grafana

An Ansible role that deploys Graphite/Grafana application on Centos 6.x

Deploy order:
  1) modify requirements.yml with your SVN username/password
  2) ansible-galaxy install -r requirements.yml
  3) ansible-playbook -i hosts playbook.yml --ask-pass

After successful installation, you  should be able to log in to:

 http://remote_host:3000    - Grafana using default admin/admin credentials
 http://remote_host:5000    - Graphite

If "Metrics" folder is empty in Graphite:
    check that local_settings.py appends correct sys.path (system python).
    Should not return any errors: python -c "import sys; sys.path.append('/usr/lib64/python2.6/site-packages/'); import rrdtool"
    RRD_DIR in local_settings.py points to correct location.

After installation, run once from the target server: {{ install_prefix }}/bin/create_symlinks.py.
That will create symlinks to {{ graphite_rrd }} for already existed files in {{ apps_rrd_path }}.
Symlink will be created automatically for every new file in {{ apps_rrd_path }}.

## Requirements

This role is depend on conda ansible role. You should install dependency using ansible-galaxy.

System packages should be pre-installed: "libXrender", "libXext", "cairo-devel", "rrdtool-devel", "rrdtool", "python-rrdtool", "bitmap-console-fonts",

Also, conda environment will use "python-rrdtool" package from system python (see local_settings.py)

## Role Variables

Available variables are listed below, along with default values:
		
	ssh_user = yanko 
	conda_packages  = 'django=1.7.1 uwsgi nginx pip whisper python-ldap pyparsing pytz python-memcached libxml2 txamqp fontconfig py2cairo simplejson'
	install_prefix = '/opt/graphite'

Modify "install_prefix", "ssh_user" variables in hosts file

## Dependencies

- http://svn/svn/ansible/common/conda/  - install and configure conda environment on the remote host
- http://svn/svn/ansible/common/supervisor/  - install and configure supervisor on the remote host

## Example Playbook

Please refer to  playbook.yml for more details
