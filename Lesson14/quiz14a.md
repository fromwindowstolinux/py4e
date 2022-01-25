# Quiz: XML

1. What is "serialization" when we are talking about web services?
- Making it so that dictionaries can maintain their keys in sorted order
- The act of taking data stored in a program and formatting it so it can be sent across the network
- Sorting all the data stored in a tuple
- Marking each network packet so it can be put back into order on the receiving system

2. What is the name of the Python library to parse XML data?
- xml2
- xml.etree.ElementTree
- xml.json
- xml-misc

3. Which of the following are not commonly used serialization formats?
- HTTP
- Dictionaries
- TCP
- XML
- JSON

4. What is the method to cause Python to parse XML that is stored in a string?
- xpath()
- readall()
- extract()
- fromstring()
- parse()

5. In this XML, which are the "complex elements"?
```
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <person>
       <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>
```
- Noah
- name
- phone
- people
- person

6. In this XML, which are the "simple elements"?
```
<people>
    <person>
       <name>Chuck</name>
       <phone>303 4456</phone>
    </person>
    <<person>
           <name>Noah</name>
       <phone>622 7421</phone>
    </person>
</people>
```
- Noah
- name
- phone
- people
- person

7. In the following XML, which are attributes?
```
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>
```
- email
- person
- name
- type
- hide

8. In the following XML, which node is the parent node of node e
```
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
```
- a
- c
- e
- b

9. Looking at the following XML, what text value would we find at path "/a/c/e"
```
<a>
  <b>X</b>
  <c>
    <d>Y</d>
    <e>Z</e>
  </c>
</a>
```
- e
- b
- a
- Z
- Y

10. What is the purpose of XML Schema?
- A Python program to tranform XML files
- To establish a contract as to what is valid XML
- To compute SHA1 checksums on data to make sure it is not modified in transit
- To transfer XML data reliably during network outages

11. If you were building an XML Schema and wanted to limit the values allowed in an xs:string field to only those in a particular list, what XML tag would you use in your XML Schema definition?
- maxOccurs
- xs:complexType
- xs:element
- xs:enumeration
- xs:sequence

12. For this XML Schema:
```
<xs:complexType name=”person”>
  <xs:sequence>
    <xs:element name="lastname" type="xs:string"/>
    <xs:element name="age" type="xs:integer"/>
    <xs:element name="dateborn" type="xs:date"/>
  </xs:sequence>
</xs:complexType>
And this XML,
<person>
   <lastname>Severance</lastname>
   <Age>17</Age>
   <dateborn>2001-04-17</dateborn>
</person>
```
Which tag is incorrect?
- dateborn
- person
- lastname
- Age
- age

13. What does the "Z" mean in this representation of a time:
```
2002-05-30T09:30:10Z
```
- The local timezone for this time is New Zealand
- This time is in the UTC timezone
- This time is Daylight Savings Time
- The hours value is in the range 0-12

14. What is a good time zone to use when computers are exchanging data over APIs?
- The local time zone of the receiving computer
- Universal Time / GMT
- The local time zone of the sending computer without daylight savings time
- The local time zone of the sending computer

15. Which of the following dates is in ISO8601 format?
- 05/30/2002
- 2002-05-30T09:30:10Z
- May 30, 2002
- 2002-May-30