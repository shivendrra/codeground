#include <iostream>
using namespace std;

class Book {
  public:
    string title;
    string author;
    int pages;
    int volumes;

    Book() {
      title = "Murder on the Orient Express";
      author = "Agatha Christie";
      pages = 150;
      volumes = 1;
    }

    Book(string aTitle, string aAuthor, int aPages, int aVolumes) {
      title = aTitle;
      author = aAuthor;
      pages = aPages;
      volumes = aVolumes;
    }
};

int main() {
  Book book1("Harry Potter", "JK Rowling", 500, 7);
  Book book2("Lord of the Rings", "JRR Tolkein", 1000, 3);
  Book book3;

  cout<< book1.title <<endl;
  cout<< book1.author <<endl;
  cout<< book1.pages <<endl;
  cout<< book1.volumes <<endl;

  cout<< book2.title <<endl;
  cout<< book2.author <<endl;
  cout<< book2.pages <<endl;
  cout<< book2.volumes <<endl;

  cout<< book3.title <<endl;
  cout<< book3.author <<endl;
  cout<< book3.pages <<endl;
  cout<< book3.volumes <<endl;
  
  return 0;
}