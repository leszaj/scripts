#ifndef MD5_GENERATOR_H
#define MD5_GENERATOR_H

#include <QAbstractListModel>
#include <QCryptographicHash>

class md5_generator : public QObject
{
    Q_OBJECT

public:
    md5_generator(QObject *parent = nullptr);
    md5_generator(const QByteArray str) { this->update(str); }

    QString hash;

    void update(const QByteArray str)    {
        this->hash = QString(QCryptographicHash::hash(str, QCryptographicHash::Md5).toHex());
    }

private:

};

#endif // MD5_GENERATOR_H


