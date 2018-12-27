import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('distro, package', [
    ('centos,debian,ubuntu', 'powertop'),
])
def test_resource_monitor_packages_are_installed(host, distro, package):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    assert host.package(package).is_installed


@pytest.mark.parametrize('distro, package', [
    ('centos,debian,ubuntu', 'nmap'),
])
def test_network_monitor_packages_are_installed(host, distro, package):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    assert host.package(package).is_installed


@pytest.mark.parametrize('distro, package', [
    ('centos,debian,ubuntu', 'tmux'),
])
def test_terminal_packages_are_installed(host, distro, package):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    assert host.package(package).is_installed


@pytest.mark.parametrize('distro, package', [
    ('centos,debian,ubuntu', 'zsh'),
])
def test_shell_packages_are_installed(host, distro, package):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    assert host.package(package).is_installed


@pytest.mark.parametrize('distro, package', [
    ('centos', 'vim-enhanced'),
    ('debian,ubuntu', 'vim'),
])
def test_editor_packages_are_installed(host, distro, package):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    assert host.package(package).is_installed
