import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.15


Window {
    width: 640
    height: 100
    visible: true
    title: qsTr("MD5 Hash Calculator")

    TextField {
        id: textField
        objectName: "inputText"
        x: 20
        y: 0
        width: 600
        height: 30
        font.pixelSize: 18
        //color: "blue"
        //font.family: "Helvetica"
        placeholderText: "Enter Text Here"
        onTextChanged: g.hash = text
    }

    TextArea {
        id: textArea
        objectName: "outputText"
        x: 20
        y: 40
        width: 600
        height: 30
        font.pointSize: 16
        color: "red"
        text: g.hash
        readOnly: true
    }
}

