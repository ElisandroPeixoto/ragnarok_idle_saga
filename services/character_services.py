from models.db_manager import SessionLocal, Character


class CharacterService:
    @staticmethod
    def create_character(name: str, job: str = "Novice"):
        """Create a new character in the database."""

        try:
            if not name or not name.strip():
                return {
                    "success": False,
                    "message": "Character name cannot be empty."
                }
            
            name = name.strip()
            db = SessionLocal()

            existing_character = db.query(Character).filter(Character.name == name).first()
            if existing_character:
                db.close()
                return {
                    "success": False,
                    "message": f"Character with name '{name}' already exists."
                }
            
            new_character = Character(name=name, job=job)
            
            db.add(new_character)
            db.commit()
            db.refresh(new_character)
            db.close()

            return {
                "success": True,
                "message": f"Character '{name}' created successfully!",
                "character": new_character
            }
        
        except Exception as e:
            return {
                "success": False,
                "message": "An error occurred while creating the character."
            }

    @staticmethod
    def delete_character(char_name: str):
        """Delete a character from the database"""
        db = SessionLocal()

        character = db.query(Character).filter(Character.name == char_name).first()

        character_to_be_deleted = character.name

        db.delete(character)
        db.commit()
        db.close()

        return {
            "success": True,
            "message": f'Character {character_to_be_deleted} deleted successfully'
        }
        