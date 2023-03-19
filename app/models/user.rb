class User < ApplicationRecord
  has_many :blogs, dependent: :destroy
  has_many :favorites, dependent: :destroy
  mount_uploader :image, ImageUploader
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable


  validates :name, uniqueness: true
  validates :name, length: { in: 2..20 }
end
