![mixed nuts](ding_dong_mixed_nuts_hot_and_spicy.jpeg)

How to install on a Raspberry Pi
--------------------------------

- Move the files in `/etc` to the same location on the raspberry pi filesystem.
- Run `sudo systemctl daemon-reload && sudo systemctl enable doorbell.service && sudo systemctl start doorbell.service`.

To view the logs, run `sudo journalctl -u doorbell`.
