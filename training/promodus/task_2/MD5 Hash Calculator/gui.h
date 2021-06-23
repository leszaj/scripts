#ifndef GUI_H
#define GUI_H

#include <QObject>
#include <QDebug>

#include "md5_generator.h"


class gui : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString hash READ hash WRITE set_hash NOTIFY hash_was_changed)

public:
    gui() : m_hash("MD5 calculation will start automatically") { };

    md5_generator md5 = md5_generator("");
    QString m_hash;
    QString hash() const    {  return m_hash;    }

    void set_hash(const QString& value) {
        if(m_hash != value) {
            md5.update(value.toUtf8());
            m_hash = this->md5.hash;
            hash_was_changed();
        }
    }

signals:
    void hash_was_changed();
};

#endif // GUI_H
