#/usr/bin/bash

# Bash script that pulls most recent Minecraft Databackups and extract the world information for further processing.
# Working Directory = /var/minecraft-map

#Vanilla Variables
v_www_output="/mnt/nfs/darkwindcraft/mcmaps/vanilla-www"
v_zip_output="/var/minecraft-map/vanilla-raw"
v_zip_input=`ls -t /mnt/nfs/darkwindcraft/Vanilla/Databackup/*.zip | head -1`

# Pixelmon Variables
p_www_output="/mnt/nfs/darkwindcraft/mcmaps/pixelmon-www"
p_zip_output="/var/minecraft-map/pixelmon-raw"
p_zip_input=`ls -t /mnt/nfs/darkwindcraft/Pixelmon/Databackup/*.zip | head -1`

# Arckeya Variables
a_www_output="/mnt/nfs/darkwindcraft/mcmaps/arckeya-www"
a_zip_output="/var/minecraft-map/arckeya-raw"
a_zip_input=`ls -t /mnt/nfs/arckeya/minecraft/databackups/*.zip | head -1`

# unzip vanilla
echo "Decompresing $v_zip_input to $v_zip_output"
unzip -qou $v_zip_input -d $v_zip_output

# unzip pixelmon
echo "Decompresing $p_zip_input to $p_zip_output"
unzip -qou $p_zip_input -d $p_zip_output

# unzip arckeya
echo "Decompresing $a_zip_input to $a_zip_output"
unzip -qou $a_zip_input -d $a_zip_output

# Fixing permissions
chmod 777 $p_www_output
chmod 777 $v_www_output
chmod 777 $a_www_output

# Pull latest docker image for updates
docker pull mide/minecraft-overviewer:latest

# Run container for rendering Vanilla
docker run --rm \
-e MINECRAFT_VERSION="1.14.1" \
-v /etc/docker/compose/minecraft-map/config.py:/home/minecraft/config.py:ro \
-v $v_zip_output:/home/minecraft/server/:ro \
-v $v_www_output:/home/minecraft/render/:rw \
mide/minecraft-overviewer:latest

# Run container for rendering Pixelcraft
docker run --rm \
-e MINECRAFT_VERSION="1.12.2" \
-v /etc/docker/compose/minecraft-map/config.py:/home/minecraft/config.py:ro \
-v $p_zip_output:/home/minecraft/server/:ro \
-v $p_www_output:/home/minecraft/render/:rw \
mide/minecraft-overviewer:2019-01

# Run container for rendering Arckeya
docker run --rm \
-e MINECRAFT_VERSION="1.14.1" \
-v /etc/docker/compose/minecraft-map/config.py:/home/minecraft/config.py:ro \
-v $a_zip_output:/home/minecraft/server/:ro \
-v $a_www_output:/home/minecraft/render/:rw \
mide/minecraft-overviewer:latest
