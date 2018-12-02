# How-To Metin2-Patcher
by martysama0134

### INFOs
1. You need the `metin2launch.bin` you can find from the official Metin2 client! (I used the latest version)
1. It works only with 7za.exe v9. I tried with 7za.exe v18, but it will keep the old files inside the binary.
1. The real index.html files for web/ can be dumped by using Save Page WE (Chrome extension)
1. The sourcefiles of mt2lz.exe can be found in [here](https://github.com/martysama0134/mt2lz)
1. No copyrighted files is present inside this repository.

### STEP1 - TORRENT PATCHER GENERATOR
1. copy the `metin2launch.bin` from the official client inside this folder
1. run `Unzip_Patcher.bat` to generate the `patcher/` folder
1. inside `patcher/TorrentPatch.url.xml` edit `remoteConfigPath` with your website URL
1. inside `patcher/TorrentPatch.locale.xml` edit `LAUNCHER_IFRAME` with your website URL (patch page)
1. inside `patcher/TorrentPatch.locale.xml` edit `LAUNCHER_NEW_URL` and `URL_NEW` with your website URL (account registration page)
1. run `Make_Patcher.bat` to generate `metin2launch.exe` (it combines `metin2launch.bin` + `patcher/` data)

### STEP2 - WEB CONFIGURATION
1. edit the `web/metin2torrent_gfl.config.xml` file by replacing `127.0.0.1` contained in `crcpatch_url` and `notice_url` with your ip/domain.
1. upload `web/` into your webhosting

### STEP3 - GENERATING THE PATCHES
1. place the files you want to patch (except `metin2launch.exe`) inside the `client/` folder
1. run crclist_maker.py or .bat or alternative .bat
1. upload the new files generated inside `web/` into your webhosting
