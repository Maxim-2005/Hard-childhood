import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Universal

ApplicationWindow {
    id: id_window
    width: 600
    height: 400
    visible: true

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        // Ввод текста
        Rectangle {
            Layout.preferredWidth: 200
            Layout.preferredHeight: 36

            TextField {
                id: id_input
                anchors.fill: parent
                font.pixelSize: 20
            }
        }

        // Кнопка
        Button {
            id: id_button
            font.pixelSize: 20
            text: "ТЕСТ КНОПКИ"

            onClicked: {
                id_button.text = "КНОПКА НАЖАТА";
                control.press_button(id_input.text);
            }
        }

        // Вывод текста
        Text {
            id: id_text
            font.pixelSize: 20
            text: "НАЧАЛЬНЫЙ ТЕКСТ В QML"
        }
        
        // Список элементов
        ListView {
            id: id_list
            width: 200
            height: 200

            model: ListModel {} // создаем модель списка
            delegate: Text {
                text: msg // текст элемента списка
            }
        }
    }

    // Прием данных
    Connections {
        target: control

        function onConnect(msg) {
            id_text.text = msg
        }

        function onAdd_item(msg) {
            id_list.model.append({"msg": msg}) // добавляем элемент в список
            id_input.text = null // очищаем после ввода
        }
    }
}