#!/bin/bash
#filename=push_clip_to_DUT.sh
if [ "$#" -ne 2 ]
then
	echo "Usage:./push_clip_to_DUT.sh device_num component"
	echo "component:APP_Decode,WIDI,HDMI,HDMI_full,video_editor,Widevine"
	exit
fi
case "$2" in
	APP_Decode)
		adb -s $1 shell mkdir /sdcard/APP_Decode
		adb -s $1 push ./BAT_playback/ /sdcard/APP_Decode/
		;;
	WIDI)
		adb -s $1 shell mkdir /sdcard/WIDI
		adb -s $1 push ./WIDI_clips/ /sdcard/WIDI/
		;;
	HDMI)
		adb -s $1 shell mkdir /sdcard/HDMI
		adb -s $1 install -r /home/hongcai/Tools/Moboplayer.x86.apk
		adb -s $1 push ./APP_PostProcess_Clips/HDMI_clips/ /sdcard/HDMI/
		;;
	HDMI_full)
		adb -s $1 shell mkdir /sdcard/HDMI
		adb -s $1 install -r /home/hongcai/Tools/Moboplayer.x86.apk
		adb -s $1 push ./APP_PostProcess_Clips/HDMI_full_clips/ /sdcard/HDMI/
		;;
	video_editor)
		adb -s $1 shell mkdir /sdcard/video_editor
		adb -s $1 push ./video_editor_clips/ /sdcard/video_editor/
		;;
	Widevine)
		adb -s $1 shell mkdir /sdcard/Widevine
		adb -s $1 install -r ../tools/WidevineSamplePlayer.apk
		adb -s $1 push ./media_showstopper_BAT/CPM-HDCP/sintel_main_720p_4br_tp.wvm /sdcard/Widevine/
		;;
	*)
		exit
		;;
esac
adb -s $1 shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///mnt/sdcard/
