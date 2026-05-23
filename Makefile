all:
	@echo "Available options:"
	@echo "install: Install the Sense Hat IP shower to the system (root)"
	@echo "uninstall: Uninstall the Sense Hat IP shower (root)"

.PHONY: install uninstall

check_root:
	@if [ "$$(id -u)" -ne 0 ]; then \
		echo "This action requires root. Please run: sudo make $(MAKECMDGOALS)"; \
		exit 1; \
	fi

install: check_root
	@printf "  %-8s %s\n" "INSTALL" "/usr/sbin/show_ip.py"
	@cp show_ip.py /usr/sbin 
	@printf "  %-8s %s\n" "INSTALL" "/etc/systemd/system/show_ip_sensehat.service"
	@cp show_ip_sensehat.service /etc/systemd/system
	@echo "Installed. To enable the service, run: systemctl enable show_ip_sensehat"

uninstall: check_root
	@printf "  %-8s %s\n" "DISABLE_SERVICE" "show_ip_sensehat"
	@systemctl disable --now show_ip_sensehat
	@printf "  %-8s %s\n" "UNINSTALL" "/usr/sbin/show_ip.py"
	@rm -f /usr/sbin/show_ip.py
	@printf "  %-8s %s\n" "UNINSTALL" "/etc/systemd/system/show_ip_sensehat.service"
	@rm -f /etc/systemd/system/show_ip_sensehat.service
	@echo "Uninstall successful."