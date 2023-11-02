"""Tests for the GogoGate2 component."""

from ismartgate.common import (
    DoorMode,
    DoorStatus,
    GogoGate2Door,
    GogoGate2InfoResponse,
    ISmartGateDoor,
    ISmartGateInfoResponse,
    Network,
    Outputs,
    Wifi,
)


def _mocked_gogogate_open_door_response():
    return GogoGate2InfoResponse(
        user="user1",
        gogogatename="gogogatename0",
        model="gogogate2",
        apiversion="",
        remoteaccessenabled=False,
        remoteaccess="abc123.blah.blah",
        firmwareversion="222",
        apicode="",
        door1=GogoGate2Door(
            door_id=1,
            permission=True,
            name="Door1",
            gate=False,
            mode=DoorMode.GARAGE,
            status=DoorStatus.OPENED,
            sensor=True,
            sensorid=None,
            camera=False,
            events=2,
            temperature=None,
            voltage=40,
        ),
        door2=GogoGate2Door(
            door_id=2,
            permission=True,
            name=None,
            gate=True,
            mode=DoorMode.GARAGE,
            status=DoorStatus.UNDEFINED,
            sensor=True,
            sensorid=None,
            camera=False,
            events=0,
            temperature=None,
            voltage=40,
        ),
        door3=GogoGate2Door(
            door_id=3,
            permission=True,
            name=None,
            gate=False,
            mode=DoorMode.GARAGE,
            status=DoorStatus.UNDEFINED,
            sensor=True,
            sensorid=None,
            camera=False,
            events=0,
            temperature=None,
            voltage=40,
        ),
        outputs=Outputs(output1=True, output2=False, output3=True),
        network=Network(ip=""),
        wifi=Wifi(SSID="", linkquality="", signal=""),
    )


def _mocked_ismartgate_closed_door_response():
    return ISmartGateInfoResponse(
        user="user1",
        ismartgatename="ismartgatename0",
        model="ismartgatePRO",
        apiversion="",
        remoteaccessenabled=True,
        remoteaccess="abc321.blah.blah",
        firmwareversion="555",
        pin=123,
        lang="en",
        newfirmware=False,
        door1=ISmartGateDoor(
            door_id=1,
            permission=True,
            name="Door1",
            gate=False,
            mode=DoorMode.GARAGE,
            status=DoorStatus.CLOSED,
            sensor=True,
            sensorid=None,
            camera=False,
            events=2,
            temperature=None,
            enabled=True,
            apicode="apicode0",
            customimage=False,
            voltage=40,
        ),
        door2=ISmartGateDoor(
            door_id=2,
            permission=True,
            name="Door2",
            gate=True,
            mode=DoorMode.GARAGE,
            status=DoorStatus.CLOSED,
            sensor=True,
            sensorid=None,
            camera=False,
            events=2,
            temperature=None,
            enabled=True,
            apicode="apicode0",
            customimage=False,
            voltage=40,
        ),
        door3=ISmartGateDoor(
            door_id=3,
            permission=True,
            name=None,
            gate=False,
            mode=DoorMode.GARAGE,
            status=DoorStatus.UNDEFINED,
            sensor=True,
            sensorid=None,
            camera=False,
            events=0,
            temperature=None,
            enabled=True,
            apicode="apicode0",
            customimage=False,
            voltage=40,
        ),
        network=Network(ip=""),
        wifi=Wifi(SSID="", linkquality="", signal=""),
    )
