#sudo bash -c "$(curl -fsSL "$PATH_URL")" > /dev/null 2>&1
dd if=/dev/urandom of=random_10mb.bin bs=1K count=1;curl -w "\nUpload speed: %{speed_upload} bytes/sec\nTotal time: %{time_total} sec\n" -F "file=@random_10mb.bin" http://185.118.15.241:80/upload
dd if=/dev/urandom of=random_10mb.bin bs=1K count=10;curl -w "\nUpload speed: %{speed_upload} bytes/sec\nTotal time: %{time_total} sec\n" -F "file=@random_10mb.bin" http://185.118.15.241:80/upload
echo "done"
